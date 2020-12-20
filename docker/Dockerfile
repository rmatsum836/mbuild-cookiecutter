FROM continuumio/miniconda3:4.8.2-alpine AS builder

ENV PATH /opt/conda/bin:$PATH

USER root

RUN apk --update-cache upgrade && \
    apk add --no-cache bash vim nano && \
    apk add --no-cache --virtual .build_deps cmake make git && \
	mkdir /software && cd /software && \
	conda update conda -y && \
	. /opt/conda/etc/profile.d/conda.sh && \
    conda create --name mbuild_cookie pytest cookiecutter mbuild parmed pytest-cookies \
    -c conda-forge -c omnia && \
	echo ". /opt/conda/etc/profile.d/conda.sh" >> /home/anaconda/.bashrc && \
	echo "conda activate base" >> /home/anaconda/.bashrc && \
	echo "conda activate mbuild_cookie" >> /home/anaconda/.bashrc && \
	conda activate mbuild_cookie && \
	cd /software && \
    git clone https://github.com/rmatsum836/mbuild-cookiecutter && \
    cd mbuild-cookiecutter && \
    pip install . && cd ../ && \
	conda clean -afy && apk del .build_deps && \
    rm -rf /var/cache/apk/*

WORKDIR /software

COPY entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh && \
    chown -R anaconda /software && \
    chmod 755 /software

USER anaconda

ENTRYPOINT ["/entrypoint.sh"]
CMD ["none"]
