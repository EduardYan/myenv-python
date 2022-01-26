# using python3 with alpine 3.15
FROM python:alpine3.15

# dependencies globals
RUN apk add --no-cache gcc musl-dev linux-headers \
    libffi-dev sqlite git curl tmux vim && pip install --upgrade pip

# modules for use in python
RUN pip install Flask SQLAlchemy rich colorama \
    ipython bcrypt requests

# configuration for vim
WORKDIR /root/
COPY vim .
RUN mkdir .vim && mv maps.vim plugins.vim .vim \
    && curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
        https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

# shell launching
CMD ["/bin/sh"]