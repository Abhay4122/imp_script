import os

def prin(*args):
    for i in args:
        print(f'\n{i}')

prin('Running the script','Setting up alias \'Hello\'')


def append_git_alias():
    os.system(
        '''
            echo "
                # Alias for ls cmd
                alias git='g'
            " >> ~/.bashrc
        '''
    )

    prin('alias helo=ls applied successfully')


def apply_commands():
    # Set alias for git
    # append_git_alias()

    # Reload the bash shell
    os.system('source ~/.bashrc')



if os.environ.get('apply_sh'):
    prin('This shell script is applied already')
    apply_commands()
else:
    os.system('export apply_sh="ok"')
    apply_commands()

