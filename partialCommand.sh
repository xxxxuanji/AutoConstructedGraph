# python ./biobert-master/relationstract.py --nes1=new_about/genes.tsv  --nes1name=gene --nes2=new_about/genes.tsv  --nes2name=gene  --paper=./new_about/new_paper_clause.txt --fileout_dir=./new_about/ge_ge
# python ./biobert-master/relationstract.py --nes1=new_about/dines.tsv --nes2=new_about/genes.tsv --nes1name=disease --nes2name=gene  --paper=./new_about/new_paper_clause.txt --fileout_dir=./new_about/di_ge
# python ./biobert-master/relationstract.py --nes1=./new_about/chnes.tsv --nes2=./new_about/dines.tsv --nes1name=chemical --nes2name=disease --paper=./new_about/new_paper_clause.txt --fileout_dir=./new_about/ch_di
# python ./biobert-master/relationstract.py --nes1=./new_about/chnes.tsv --nes2=./new_about/genes.tsv --nes1name=chemical --nes2name=gene --paper=./new_about/new_paper_clause.txt --fileout_dir=./new_about/ch_ge
# #将new_paper_test.txt(逐个句子)，dines.tsv(疾病实体)和genes.tsv(基因实体)作为输入,观察每个句子中是否同时包含这二者，若同时包含，则选出这个句子，并标记好两种实体所出现的位置，将所有选出的句子输出到/di_ge/test.tsv中。

# python ./biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=/home/tby/lyc/re_output/GNBR_output/cd/alleviates/model.ckpt-2343 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/ch_di --output_dir=./re_output/cd/alleviates/
# python ./biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=/home/tby/lyc/re_output/GNBR_output/cd/inhibits-cell-growth/model.ckpt-562 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/ch_di --output_dir=./re_output/cd/inhibits-cell-growth/
# python ./biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=/home/tby/lyc/re_output/GNBR_output/cd/prevents/model.ckpt-2343 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/ch_di --output_dir=./re_output/cd/prevents/
# python ./biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=/home/tby/lyc/re_output/GNBR_output/cd/role-in-disease-pathogenesis/model.ckpt-562 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/ch_di --output_dir=./re_output/cd/role-in-disease-pathogenesis/
# python ./biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=/home/tby/lyc/re_output/GNBR_output/cd/side-effect/model.ckpt-562 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/ch_di --output_dir=./re_output/cd/side-effect/
# python ./biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=/home/tby/lyc/re_output/GNBR_output/cd/treatment/model.ckpt-2343 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/ch_di --output_dir=./re_output/cd/treatment/
# python ./biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=/home/tby/lyc/re_output/GNBR_output/cg/affects-expression/model.ckpt-562 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/ch_ge --output_dir=./re_output/cg/affects-expression/
# python ./biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=/home/tby/lyc/re_output/GNBR_output/cg/agonism/model.ckpt-2109 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/ch_ge --output_dir=./re_output/cg/agonism/
# python ./biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=/home/tby/lyc/re_output/GNBR_output/cg/antagonism/model.ckpt-2109 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/ch_ge --output_dir=./re_output/cg/antagonism/
# python ./biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=/home/tby/lyc/re_output/GNBR_output/cg/binding/model.ckpt-2109 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/ch_ge --output_dir=./re_output/cg/binding/
# python ./biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=/home/tby/lyc/re_output/GNBR_output/cg/decreases-expression/model.ckpt-562 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/ch_ge --output_dir=./re_output/cg/decreases-expression/
# python ./biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=/home/tby/lyc/re_output/GNBR_output/dg/biomarkers/model.ckpt-2109 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/di_ge --output_dir=./re_output/dg/biomarkers/
# python ./biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=/home/tby/lyc/re_output/GNBR_output/dg/improper-regulation-linked-to-disease/model.ckpt-562 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/di_ge --output_dir=./re_output/dg/improper-regulation-linked-to-disease/
# python ./biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=/home/tby/lyc/re_output/GNBR_output/dg/overexpression-in-disease/model.ckpt-562 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/di_ge --output_dir=./re_output/dg/overexpression-in-disease/
# python ./biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=/home/tby/lyc/re_output/GNBR_output/gg/activates/model.ckpt-2109 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/ge_ge --output_dir=./re_output/gg/activates/
# python ./biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=/home/tby/lyc/re_output/GNBR_output/gg/binding/model.ckpt-2109 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/ge_ge --output_dir=./re_output/gg/binding/
# python ./biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=/home/tby/lyc/re_output/GNBR_output/gg/regulation/model.ckpt-2109 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/ge_ge --output_dir=./re_output/gg/regulation/
# python ./tbytordf_ch_di.py
# python ./tbytordf_ch_ge.py
# python ./tbytordf_di_ge.py
# python ./tbytordf_ge_ge.py
# python ./tbytoneo_ch_di.py
# python ./tbytoneo_ch_ge.py
# python ./tbytoneo_di_ge.py
# python ./tbytoneo_ge_ge.py 
python ./predict_conflict_find.py
python ./conflict_solve.py