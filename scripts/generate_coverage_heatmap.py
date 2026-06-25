import json
import matplotlib.pyplot as plt
import seaborn as sns

def generate_heatmap(
    control_set_name, 
    control_set_path, 
    output_path
):
    # Load control set
    with open(control_set_path, 'r') as f:
        controls = json.load(f)
    
    # Create a simple presence matrix (dummy data example)
    matrix = [[1 if 'control_a' in control else 0 for control in controls],
              [1 if 'control_b' in control else 0 for control in controls],
              [1 if 'control_c' in control else 0 for control in controls]]
    
    # Create heatmap
    sns.set(font_scale=1.2)
    plt.figure(figsize=(10, 8))
    sns.heatmap(matrix, cmap='viridis', xticklabels=controls, yticklabels=['Category 1', 'Category 2', 'Category 3'])
    plt.title(f'Control Coverage Heatmap - {control_set_name}')
    plt.savefig(output_path)
    plt.close()

if __name__ == '__main__':
    generate_heatmap(
        control_set_name='sp80053',
        control_set_path='/tmp/placeholder_sp80053_controls.json',
        output_path='/srv/tyche/projects/limen-ai-edge-case-atlas/results/boost/limen-boost-036/coverage_heatmap_v2.svg'
    )