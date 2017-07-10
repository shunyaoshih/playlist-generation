""" arguments definition """

import argparse

def params_setup():
    """ arguments definition """

    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', type=str, default='train', help='')
    parser.add_argument('--attention_mode', type=str, default='bahdanau', help='')
    parser.add_argument('--learning_rate', type=float, default=0.5, help='')
    parser.add_argument('--max_gradient_norm', type=float, default=5.0, help='')
    parser.add_argument('--num_units', type=int, default=128, help='')
    parser.add_argument('--num_layers', type=int, default=3, help='')
    parser.add_argument('--batch_size', type=int, default=32, help='')
    parser.add_argument('--encoder_vocab_size', type=int, default=30000, help='')
    parser.add_argument('--decoder_vocab_size', type=int, default=86000, help='')
    parser.add_argument('--embedding_size', type=int, default=128, help='')
    parser.add_argument('--encoder_max_len', type=int, default=52, help='')
    parser.add_argument('--decoder_max_len', type=int, default=420, help='')


    args = parser.parse_args()

    return args
