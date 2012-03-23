" vimrc by Godson@ustcbbs
" Last Update: 2010-02-08




set fenc=utf-8
set nocompatible    " 关闭兼容模式
syntax enable       " 语法高亮
filetype plugin on  " 文件类型插件
filetype indent on
set fdm=indent
set autoindent
autocmd BufEnter * :syntax sync fromstart
set nu              " 显示行号
set showcmd         " 显示命令
set lz              " 当运行宏时，在命令执行完成之前，不重绘屏幕
set hid             " 可以在没有保存的情况下切换buffer
set backspace=eol,start,indent 
set whichwrap+=<,>,h,l " 退格键和方向键可以换行
set incsearch       " 增量式搜索
set hlsearch        " 高亮搜索
set ignorecase      " 搜索时忽略大小写
set magic           " 额，自己:h magic吧，一行很难解释
set showmatch       " 显示匹配的括号
set nobackup        " 关闭备份
set nowb
"set noswapfile      " 不使用swp文件，注意，错误退出后无法恢复
set lbr             " 在breakat字符处而不是最后一个字符处断行
set ai              " 自动缩进
set si              " 智能缩进
set cindent         " C/C++风格缩进
set wildmenu        
set nofen
set fdl=10

" tab转化为4个字符
set expandtab
set smarttab
set shiftwidth=4
set tabstop=4

" 不使用beep或flash
set vb t_vb=

set background=dark
colorscheme desert
"set t_Co=256

set history=400  " vim记住的历史操作的数量，默认的是20
set autoread     " 当文件在外部被修改时，自动重新读取
set mouse=a      " 在所有模式下都允许使用鼠标，还可以是n,v,i,c等

" 设置字符集编码，默认使用utf8
set encoding=utf8
set fileencodings=utf8,gb2312,gb18030,ucs-bom,latin1

