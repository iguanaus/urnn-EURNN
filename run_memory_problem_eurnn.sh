#!/bin/bash
niter=100
batch_size=20
learning_rate=0.001

mkdir -p exp

for t in 100; do
	for model in RNN,51,adhoc,1; do IFS=","; set $model
        SECONDS=0
        w_impl=$3
        echo "Running memory_problem experiment for N=$2 $1 with time_steps=$t"
        cmd="THEANO_FLAGS='device=gpu0' python2.7 -u memory_problem.py $niter ${batch_size} $2 $t 0.001 exp/memory_problem_$1_$3_$1_nhidden$2_t$t $1 categorical True CE $w_impl --capacity $4"
        echo $cmd
        eval $cmd
        echo "Experiment took $SECONDS seconds."
    done
done

