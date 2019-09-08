# deoplete-terminal

Terminal completion for deoplete.nvim


## Required

### deoplete.nvim(5.2+)
https://github.com/Shougo/deoplete.nvim


## Configuration

```vim
" Search background terminal buffers
call deoplete#custom#var('terminal', 'require_same_tab', v:false)
```
