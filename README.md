# what is this?

make tsv file from csv.
like this.
![sample image](/sample_tsv.png)

# setting & usage

    npm install -g cssfmt 
    git clone git@github.com:akyao/css-tools.git
    cd css-tools
    cat sample.css | cssfmt | python css2tsv.py > sample.tsv
