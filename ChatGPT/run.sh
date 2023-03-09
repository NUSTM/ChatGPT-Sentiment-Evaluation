for seed in 13 #42 550
do
    for shot_num in 3
    do
        for task in ASPE
        do
            for ds in 14res  #  14lap 
            do
                python openai_evaluate.py \
                --seed ${seed} \
                --task ${task} \
                --dataset ${ds} \
                --test_file 100_test \
                --shot_num ${shot_num} \
                --file_prefix 100_test_${shot_num}shot_seed${seed} \
                --do_few_shot
            done
        done
    done
done
