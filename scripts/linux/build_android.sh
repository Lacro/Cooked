source ./config.sh


PATH=$PATH:$miniforge_path/bin

branch_name=$(git rev-parse --abbrev-ref HEAD)
echo "Current git branch: '$branch_name'"

conda_env_name=${app_name}_${branch_name}_env
echo "Conda env : '$conda_env_name'"

conda activate $conda_env_name

cd ../..
flet build apk --output ./release/
