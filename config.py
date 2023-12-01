train_path = "data/training_data"
test_path = "data/testing_data"
batch_size = 30 #320
learning_rate = 0.0007
epochs = 100 #150
latent_dim = 512
num_encoder_tokens = 4096
num_decoder_tokens = 1500
time_steps_encoder = 80
time_steps_decoder = 80
max_probability = -1
save_model_path = 'model_final'
validation_split = 0.15
max_length = 10
search_type = 'greedy'
