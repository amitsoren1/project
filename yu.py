import subprocess, os, argparse
# os.chdir(os.path.join(os.getcwd(),"acme.sh"))
# # process = subprocess.Popen(['git', 'clone', 'https://github.com/acmesh-official/acme.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# process = subprocess.Popen(['./acme.sh','--uninstall'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# process.wait() # Wait for process to complete.

# # iterate on the stdout line by line
# for line in process.stdout.readlines():
#     print(line.decode("utf-8"))

# print("ERROR")

# for line in process.stderr.readlines():
#     print(line)

class SetupSSL:
    clone_url_command = ['git','clone','https://github.com/acmesh-official/acme.sh']
    upgrade_acme_command = ['./acme.sh','--upgrade']
    install_acme_command = ['./acme.sh','--install']
    def run_commands(self,commands):
        process = subprocess.Popen(commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        process.wait() # Wait for process to complete.

        # iterate on the stdout line by line
        outputs = []
        for line in process.stdout.readlines():
            outputs.append(line.decode("utf-8"))

        print("ERROR")

        errors_and_warnings = []
        for line in process.stderr.readlines():
            errors_and_warnings.append(line.decode("utf-8"))
        return outputs,errors_and_warnings
    
    def install_acme(self):
        try:
            self.run_commands(self.clone_url_command)
        except:
            print("already cloned")
            print("upgrading...")
            out,warn_err = self.run_commands(self.upgrade_acme_command)
            if len(warn_err) == 0:
                print("Done")
            else:
                print("An error occured while upgrading")
        
        os.chdir(os.path.join(os.getcwd(),"acme.sh"))

        out, warn_err = self.run_commands(self.install_acme_command)
        for x in out:
            print(x)


if __name__ == '__main__':
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('--d', action='store', type=str)
    my_parser.add_argument('--r', action='store', type=str)
    args = my_parser.parse_args()
    # print(vars(args))
    obj = SetupSSL()
    obj.install_acme()
