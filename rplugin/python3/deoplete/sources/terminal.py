# ============================================================================
# FILE: terminal.py
# AUTHOR: Shougo Matsushita <Shougo.Matsu at gmail.com>
# License: MIT license
# ============================================================================

from deoplete.base.source import Base
from deoplete.util import parse_buffer_pattern
from deoplete.util import Nvim, UserContext, Candidates


class Source(Base):

    def __init__(self, vim: Nvim) -> None:
        super().__init__(vim)

        self.name = 'terminal'
        self.mark = '[term]'
        self.filetypes = []
        self.vars = {
            'require_same_tab': True,
        }

    def gather_candidates(self, context: UserContext) -> Candidates:
        bufnrs = (self.vim.call('tabpagebuflist')
                  if self.get_var('require_same_tab')
                  else range(1, self.vim.call('bufnr', '$')))
        candidates: Candidates = []
        for bufnr in [x for x in bufnrs if 'terminal' in self.vim.call(
            'getbufvar', x, '&buftype')]:
            candidates += self._make_cache(context, bufnr)
        return candidates

    def _make_cache(self, context: UserContext, bufnr: int) -> Candidates:
        try:
            end = len(self.vim.buffers[bufnr])
            start = max([end - 5000, 1])
            return [{'word': x} for x in parse_buffer_pattern(
                self.vim.call('getbufline', bufnr, start, end),
                context['keyword_pattern'])]
        except:
            return []
