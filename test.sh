set -e
# 获取脚本文件所在的目录
SCRIPT_DIR=$(dirname "$(realpath "$0")")

# 切换到脚本所在目录
cd "$SCRIPT_DIR" || exit

# 打印当前工作目录（验证是否切换成功）
echo "当前工作目录: $(pwd)"
export CUDA_VISIBLE_DEVICES=2
source ~/anaconda3/etc/profile.d/conda.sh

# 起始日期和结束日期
start_date="2021-1-01"
end_date="2024-12-01"

# 转换为时间戳
current_date=$(date -d "$start_date" +%s)
end_date_ts=$(date -d "$end_date" +%s)

# 循环
while [ "$current_date" -le "$end_date_ts" ]
do
    # 格式化为可读日期
    readable_date=$(date -d "@$current_date" +"%Y/%m/%d")
    echo "Processing date: $readable_date"
    
    current_date=$readable_date
    
    new_paper_dir="./new_about/$(date -d  "$current_date" +"%Y%m%d")"
    
    conda deactivate
    conda activate languageModel
    python ./Entrance.py --date1=$current_date --date2=$current_date --mesh_file='Entries/Cancer.txt'
    file_path=$new_paper_dir/new_paper.txt
    if [ ! -s "$file_path" ]; then
    echo "文件 $file_path 是空的，退出程序。"
    exit 1
    fi
    echo "文件 $file_path 存在且不为空，继续执行脚本。"
    python ./modify_paper.py --date=$current_date
    python ../biobert-master/standoff2conll/standoff2conll.py $new_paper_dir/new_paper_clause.txt  --wfilename=$new_paper_dir/paper.tsv
    python ./modify_test.py  --paper_file=$new_paper_dir/paper.tsv  --output_file=new_about/test.tsv

    python ../biobert-master/run_ner.py --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=../biobert-master/ner_outputs_di/model.ckpt-1983 --num_train_epochs=10.0 --data_dir=./new_about --output_dir=./ner_outputs_di
    python ../biobert-master/run_ner.py --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=../biobert-master/ner_outputs_ch/model.ckpt-19162 --num_train_epochs=10.0 --data_dir=./new_about --output_dir=./ner_outputs_ch
    python ../biobert-master/run_ner.py --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=../biobert-master/ner_outputs_ge/model.ckpt-4716 --num_train_epochs=10.0 --data_dir=./new_about --output_dir=./ner_outputs_ge

    python ../biobert-master/biocodes/ner_detokenize.py --token_test_path=./ner_outputs_di/token_test.txt --label_test_path=./ner_outputs_di/label_test.txt --answer_path=new_about/test.tsv --output_dir=./ner_outputs_di
    python ../biobert-master/biocodes/ner_detokenize.py --token_test_path=./ner_outputs_ch/token_test.txt --label_test_path=./ner_outputs_ch/label_test.txt --answer_path=new_about/test.tsv --output_dir=./ner_outputs_ch
    python ../biobert-master/biocodes/ner_detokenize.py --token_test_path=./ner_outputs_ge/token_test.txt --label_test_path=./ner_outputs_ge/label_test.txt --answer_path=new_about/test.tsv --output_dir=./ner_outputs_ge
    python ../biobert-master/token2word.py --data_dir=./ner_outputs_ch --fileout_dir=new_about/chnes.tsv
    python ../biobert-master/token2word.py --data_dir=./ner_outputs_di --fileout_dir=new_about/dines.tsv
    python ../biobert-master/token2word.py --data_dir=./ner_outputs_ge --fileout_dir=new_about/genes.tsv
    python ../biobert-master/relationstract.py --nes1=new_about/dines.tsv --nes2=new_about/genes.tsv --nes1name=disease --nes2name=gene --paper=$new_paper_dir/new_paper_clause.txt --fileout_dir=new_about/di_ge
    python ../biobert-master/relationstract.py --nes1=new_about/chnes.tsv --nes2=new_about/dines.tsv --nes1name=chemical --nes2name=disease --paper=$new_paper_dir/new_paper_clause.txt --fileout_dir=new_about/ch_di
    python ../biobert-master/relationstract.py --nes1=new_about/chnes.tsv --nes2=new_about/genes.tsv --nes1name=chemical --nes2name=gene --paper=$new_paper_dir/new_paper_clause.txt --fileout_dir=new_about/ch_ge
    python ../biobert-master/relationstractgg.py --nes1=new_about/genes.tsv --nes1name=gene --paper=$new_paper_dir/new_paper_clause.txt --fileout_dir=new_about/ge_ge

    python ../biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=../biobert-master/GNBR_output/cd/alleviates/model.ckpt-2343 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/ch_di --output_dir=./re_output/cd/alleviates/
    python ../biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=../biobert-master/GNBR_output/cd/inhibits-cell-growth/model.ckpt-562 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/ch_di --output_dir=./re_output/cd/inhibits-cell-growth/
    python ../biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=../biobert-master/GNBR_output/cd/prevents/model.ckpt-2343 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/ch_di --output_dir=./re_output/cd/prevents/
    python ../biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=../biobert-master/GNBR_output/cd/role-in-disease-pathogenesis/model.ckpt-562 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/ch_di --output_dir=./re_output/cd/role-in-disease-pathogenesis/
    python ../biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=../biobert-master/GNBR_output/cd/side-effect/model.ckpt-562 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/ch_di --output_dir=./re_output/cd/side-effect/
    python ../biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=../biobert-master/GNBR_output/cd/treatment/model.ckpt-2343 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/ch_di --output_dir=./re_output/cd/treatment/
    python ../biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=../biobert-master/GNBR_output/cg/affects-expression/model.ckpt-562 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/ch_ge --output_dir=./re_output/cg/affects-expression/
    python ../biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=../biobert-master/GNBR_output/cg/agonism/model.ckpt-2109 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/ch_ge --output_dir=./re_output/cg/agonism/
    python ../biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=../biobert-master/GNBR_output/cg/antagonism/model.ckpt-2109 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/ch_ge --output_dir=./re_output/cg/antagonism/
    python ../biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=../biobert-master/GNBR_output/cg/binding/model.ckpt-2109 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/ch_ge --output_dir=./re_output/cg/binding/
    python ../biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=../biobert-master/GNBR_output/cg/decreases-expression/model.ckpt-562 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/ch_ge --output_dir=./re_output/cg/decreases-expression/
    python ../biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=../biobert-master/GNBR_output/dg/biomarkers/model.ckpt-2109 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/di_ge --output_dir=./re_output/dg/biomarkers/
    python ../biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=../biobert-master/GNBR_output/dg/improper-regulation-linked-to-disease/model.ckpt-562 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/di_ge --output_dir=./re_output/dg/improper-regulation-linked-to-disease/
    python ../biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=../biobert-master/GNBR_output/dg/overexpression-in-disease/model.ckpt-562 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/di_ge --output_dir=./re_output/dg/overexpression-in-disease/
    python ../biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=../biobert-master/GNBR_output/gg/activates/model.ckpt-2109 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/ge_ge --output_dir=./re_output/gg/activates/
    python ../biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=../biobert-master/GNBR_output/gg/affects-expression/model.ckpt-2109 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/ge_ge --output_dir=./re_output/gg/binding/
    python ../biobert-master/run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=../biobert-master/biobert_v1.1_pubmed/vocab.txt --bert_config_file=../biobert-master/biobert_v1.1_pubmed/bert_config.json --init_checkpoint=../biobert-master/GNBR_output/gg/regulation/model.ckpt-2109 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./new_about/ge_ge --output_dir=./re_output/gg/regulation/
    python ./tbytordf_ch_di.py --new_paper_dir=$new_paper_dir
    python ./tbytordf_ch_ge.py --new_paper_dir=$new_paper_dir
    python ./tbytordf_di_ge.py --new_paper_dir=$new_paper_dir
    python ./tbytordf_ge_ge.py  --new_paper_dir=$new_paper_dir
    python ./tbytoneo_ch_di.py --new_paper_dir=$new_paper_dir --date=$current_date
    python ./tbytoneo_ch_ge.py  --new_paper_dir=$new_paper_dir --date=$current_date
    python ./tbytoneo_di_ge.py  --new_paper_dir=$new_paper_dir  --date=$current_date
    python ./tbytoneo_ge_ge.py  --new_paper_dir=$new_paper_dir  --date=$current_date
    python ./test.py --date=$current_date
    # 日期加一天
    current_date=$(date -d "$readable_date +1 day" +%s)
    rm -rf $new_paper_dir
done
