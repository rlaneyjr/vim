cd C:/Users/rlaney/.vim_runtime

echo 'set runtimepath+=C:/Users/rlaney/.vim_runtime

source C:/Users/rlaney/.vim_runtime/vimrcs/basic.vim
source C:/Users/rlaney/.vim_runtime/vimrcs/filetypes.vim
source C:/Users/rlaney/.vim_runtime/vimrcs/plugins_config.vim
source C:/Users/rlaney/.vim_runtime/vimrcs/extended.vim

try
source C:/Users/rlaney/.vim_runtime/my_configs.vim
catch
endtry' > C:/Users/rlaney/.vimrc

echo "Installed the Ultimate Vim configuration successfully! Enjoy :-)"
