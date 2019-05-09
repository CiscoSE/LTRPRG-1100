for i in {0..15}; do for j in {1..254}; do echo 10.128.$i.$j; done; done | xargs -I {} -P5000 ping -c1 -W1 -q {}
