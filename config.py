"""
This script make 
some configurations for vim.
"""


def create_vimrc(content:list, path:str) -> None:
  """
  Create a vimrc file
  for a basic configuration.
  """

  # open the path and writing the content
  with open(path, 'w') as f:
    for line in content:
      f.write(str(line) + '\n')

    # closing the file
    f.close()




if __name__ == '__main__':
  # content to set in vimrc file
  CONTENT = [
    '" This is a basic configuration for vim',
    '" Some Mappings',
    'let mapleader=","',
    'inoremap kj <esc>',
    'nnoremap <leader>f :w!<CR>',
    'nnoremap <leader>q :q<CR>',
    '" See syntax',
    'syntax on',
    'set encoding=utf-8',
    '" No compatible with vi',
    'set nocompatible',
    'set ruler',
    'set number',
    'set hidden',
    '" always show status bar',
    'set ls=2',
    '" highlighted searh results',
    'set hlsearch',
    '" no wraping',
    'set nowrap',
    'set clipboard=unnamedplus',
    '" No swap file to edit a file',
    'set noswapfile',
    'set showcmd',
    'set noerrorbells',
    'set updatetime=300',
    '" tabs and spaces handling',
    'set tabstop=4',
    'set softtabstop=4',
    'set shiftwidth=4',
    'set expandtab',
    '" show rule in column 100',
    'set colorcolumn=100',
    '" how to split windows',
    'set splitbelow',
    'set splitright',
    'set mouse=a',
    '"show cursor line',
    'set cursorline',
    '" Better Menu',
    'set wildmenu',
    '" colors integration with tmux',
    'set t_Co=256',
    '" if exists("+termguicolors")',
    '  " let &t_8f = "\<Esc>[38;2;%lu;%lu;%lum"',
    '  " let &t_8b = "\<Esc>[48;2;%lu;%lu;%lum"',
    '  " set termguicolors',
    '" endif',
    '" search',
    'set incsearch',
    '" clear search results',
    'nnoremap <silent><space> :nohl<CR>',
    'set ignorecase',
    'set autoindent',
    'set smartcase',
  ]

  PATH_VIMRC = '/root/.vimrc'


  # creating a file of basic configuration for vim
  create_vimrc(CONTENT, PATH_VIMRC)