# Zsh configuration

# XDG base dirs
export XDG_CONFIG_HOME="$HOME/.config"
export XDG_DATA_HOME="$HOME/.local/share"
export XDG_CACHE_HOME="$HOME/.cache"

# Path
export PATH="$HOME/.local/bin:$PATH"

# History
HISTFILE="$HOME/.zsh_history"
HISTSIZE=10000
SAVEHIST=10000
setopt hist_ignore_dups
setopt hist_reduce_blanks
setopt share_history

# Completion
autoload -Uz compinit
compinit

# Key bindings
bindkey -e

# Prompt
if command -v starship >/dev/null 2>&1; then
  eval "$(starship init zsh)"
else
  autoload -Uz colors && colors
  PROMPT='%F{cyan}%n@%m%f %F{yellow}%~%f %# '
fi

# Aliases
alias ll='ls -alF'
alias la='ls -A'
alias gs='git status -sb'
alias gd='git diff'
alias gco='git checkout'
alias gl='git pull --ff-only'
alias gp='git push'

# Local overrides
[ -f "$HOME/.zshrc.local" ] && source "$HOME/.zshrc.local"
