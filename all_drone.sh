#python run.py --sg_itt 1000 --init_step 1000 --model drone --inst uniform -vo --file_out drone_uniform.txt --tol 1e-4 --save_res drone_uniform_100.txt -N 200 --to 172800 --MC --MC_p --sg_only --save_figs drone_uniform --save uniform_samples.pkl 
#python run.py --sg_itt 1000 --init_step 1000 --model drone --inst x-neg-bias -vo --file_out drone_x_neg.txt --tol 1e-4 --save_res drone_x_neg_100.txt -N 200 --MC --to 172800 --MC_p --sg_only --save_figs drone_x_neg --save x-neg_samples.pkl
python run.py --sg_itt 1000 --init_step 1000 --model drone --inst y-pos-bias -vo --file_out drone_y_pos.txt --tol 1e-4 --save_res drone_y_pos_100.txt -N 200 --MC --to 172800 --MC_p --sg_only --save_figs drone_y_pos --save y-pos_samples.pkl
