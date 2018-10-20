python retrain2.py \
--bottleneck_dir=bottlenecks \
--how_many_training_steps 100 \
--model_dir=model_dir \
--output_graph=retrained_graph.pb \
--output_labels=retrained_labels.txt \
--summaries_dir=retrain_logs \
--image_dir='/drive/GPU/recog/images_dir'

