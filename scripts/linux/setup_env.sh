source ./config.sh

PATH=$PATH:$miniforge_path/bin
#echo $PATH

branch_name=$(git rev-parse --abbrev-ref HEAD)
echo "Current git branch: '$branch_name'"

conda_env_name=${app_name}_${branch_name}_env
echo "Conda env : '$conda_env_name'"


echo =================== Check workspace ==================
if conda env list | grep $conda_env_name > /dev/null 2>&1
then
    read -p "Env '$conda_env_name' already exist, remove old python env (y/[n])? " confirm
    if [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]]; then
        create_env=true
        conda env remove -n $conda_env_name -y
    else
        create_env=false
    fi
else
    echo "env $conda_env_name dosn't exist"
    create_env=true
fi


if [ "$create_env" = true ]
then
    echo ================= Create Python env ==================
    conda create -n $conda_env_name python=$python_version -y
    conda activate $conda_env_name
    echo installing dependencies...
    pip install -r $requirements_file
    echo installed packages:
    pip list
fi

#echo ================ build VS Code projet ================
#mkdir ../.vscode


echo ======================== DONE ========================
