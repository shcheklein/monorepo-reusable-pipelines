import argparse
import yaml
from io import StringIO
import pandas as pd


parser = argparse.ArgumentParser()
parser.add_argument('--type', help='model type')
parser.add_argument('--target', help='target of data')
parser.add_argument('--params', help='path to params.yaml')
args = parser.parse_args()


def main():
    params = load_params(args.params)
    
    data_dir = f"{params['data_dir']}/{params['target']}"
    model_dir = f"{params['project']}/{params['target']}/{params['model_dir']}"
    print(data_dir)
    print(model_dir)
    
    train(
        processed_data=data_dir, 
        model_dir=model_dir, 
        model_type=args.type, 
        target=args.target
    )


def train(processed_data: str, model_dir: str, model_type: str, target: str):
    model = StringIO()
    df = pd.read_csv(f'{processed_data}/processed/data.csv', header=None)
    for _, row in df.iterrows():
        for cell in row:
            model.write(cell)
            
    model_path = f'{model_dir}/model_{model_type}_{target}.file' 
    print(model_path)
    
    with open(model_path, 'w') as f:
        f.write(model.getvalue())


def load_params(filename: str):
    with open(filename, 'r') as f:
        params = yaml.safe_load(f)
        return params 


if __name__ == '__main__':
    main()
