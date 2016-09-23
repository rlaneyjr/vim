import zipfile
import shutil
import tempfile
import requests

from os import path


#--- Globals ----------------------------------------------
PLUGINS = """
ack.vim https://github.com/mileszs/ack.vim
ag.vim https://github.com/rking/ag.vim
base16-vim https://github.com/chriskempson/base16-vim
bufexplorer https://github.com/corntrace/bufexplorer
ctrlp.vim https://github.com/kien/ctrlp.vim
dash.vim https://github.com/rizzatti/dash.vim
goyo.vim https://github.com/junegunn/goyo.vim
nerdtree https://github.com/scrooloose/nerdtree
nginx.vim https://github.com/vim-scripts/nginx.vim
open_file_under_cursor.vim https://github.com/amix/open_file_under_cursor.vim
python-mode https://github.com/klen/python-mode
rbenv-aliases https://github.com/tpope/rbenv-aliases
rbenv-ctags https://github.com/tpope/rbenv-ctags
ruby-icloud https://github.com/adammck/ruby-icloud
tComment https://github.com/vim-scripts/tComment
tlib https://github.com/vim-scripts/tlib
vim-addon-mw-utils https://github.com/MarcWeber/vim-addon-mw-utils
vim-bundle-mako https://github.com/sophacles/vim-bundle-mako
vim-bundler https://github.com/tpope/vim-bundler
vim-coffee-script https://github.com/kchmck/vim-coffee-script
vim-colors-solarized https://github.com/altercation/vim-colors-solarized
vim-commentary https://github.com/tpope/vim-commentary
vim-dotenv https://github.com/tpope/vim-dotenv
vim-endwise https://github.com/tpope/vim-endwise
vim-eunuch https://github.com/tpope/vim-eunuch
vim-expand-region https://github.com/terryma/vim-expand-region
vim-fugitive https://github.com/tpope/vim-fugitive
vim-gitgutter https://github.com/airblade/vim-gitgutter
vim-go https://github.com/fatih/vim-go
vim-indent-object https://github.com/michaeljsmith/vim-indent-object
vim-irblack https://github.com/wesgibbs/vim-irblack
vim-jdaddy https://github.com/tpope/vim-jdaddy
vim-less https://github.com/groenewege/vim-less
vim-markdown https://github.com/tpope/vim-markdown
vim-mkdir https://github.com/pbrisbin/vim-mkdir
vim-multiple-cursors https://github.com/terryma/vim-multiple-cursors
vim-pyte https://github.com/therubymug/vim-pyte
vim-rails https://github.com/tpope/vim-rails
vim-rake https://github.com/tpope/vim-rake
vim-rbenv https://github.com/tpope/vim-rbenv
vim-repeat https://github.com/tpope/vim-repeat
vim-rsi https://github.com/tpope/vim-rsi
vim-ruby https://github.com/vim-ruby/vim-ruby
vim-rvm https://github.com/tpope/vim-rvm
vim-snipmate https://github.com/garbas/vim-snipmate
vim-snippets https://github.com/honza/vim-snippets
vim-surround https://github.com/tpope/vim-surround
vim-tbone https://github.com/tpope/vim-tbone
vim-tmux-navigator https://github.com/christoomey/vim-tmux-navigator
vim-virtualenv https://github.com/jmcantrell/vim-virtualenv
vim-zenroom2 https://github.com/amix/vim-zenroom2
vimwiki https://github.com/vim-scripts/vimwiki
seti.vim https://github.com/trusktr/seti.vim
vim-easy-align https://github.com/junegunn/vim-easy-align
molokai https://github.com/tomasr/molokai
""".strip()

# Removed plugins
#vim-airline https://github.com/vim-airline/vim-airline
#vim-airline-themes https://github.com/vim-airline/vim-airline-themes
#gruvbox https://github.com/morhetz/gruvbox
#mayansmoke https://github.com/vim-scripts/mayansmoke
#peaksea https://github.com/vim-scripts/peaksea
#snipmate-snippets https://github.com/scrooloose/snipmate-snippets
#syntastic https://github.com/scrooloose/syntastic
#vim-sensible https://github.com/tpope/vim-sensible

GITHUB_ZIP = '%s/archive/master.zip'

SOURCE_DIR = path.join(path.dirname(__file__), 'plugged')


def download_extract_replace(plugin_name, zip_path, temp_dir, source_dir):
    temp_zip_path = path.join(temp_dir, plugin_name)

    # Download and extract file in temp dir
    req = requests.get(zip_path)
    open(temp_zip_path, 'wb').write(req.content)

    zip_f = zipfile.ZipFile(temp_zip_path)
    zip_f.extractall(temp_dir)

    plugin_temp_path = path.join(temp_dir,
                                 path.join(temp_dir, '%s-master' % plugin_name))

    # Remove the current plugin and replace it with the extracted
    plugin_dest_path = path.join(source_dir, plugin_name)

    try:
        shutil.rmtree(plugin_dest_path)
    except OSError:
        pass

    shutil.move(plugin_temp_path, plugin_dest_path)

    print('Updated {0}'.format(plugin_name))


if __name__ == '__main__':
    temp_directory = tempfile.mkdtemp()

    try:
        for line in PLUGINS.splitlines():
            name, github_url = line.split(' ')
            zip_path = GITHUB_ZIP % github_url
            download_extract_replace(name, zip_path,
                                     temp_directory, SOURCE_DIR)
    finally:
        shutil.rmtree(temp_directory)
