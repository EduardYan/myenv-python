# using python3 with alpine 3.15
FROM python:alpine3.15

# dependencies globals
RUN apk add --no-cache build-base ncurses-dev py3-distutils-extra musl-dev linux-headers \
    libffi-dev sqlite git curl python3-tkinter tmux \
    && pip install --upgrade pip

# modules for use in python
RUN pip install Flask SQLAlchemy rich colorama \
    ipython bcrypt requests

# build vim editor
RUN git clone https://github.com/vim/vim \
    && cd vim/src \
    && ./configure --prefix=/usr --with-python3-config-dir=/usr/lib/python3.9/config-3.9-x86_64-linux-musl \
      --enable-python3interp \
    && make && make install

WORKDIR /root/
COPY . .

# configuration for vim
RUN python3 config.py


# shell launching
CMD ["/bin/sh"]