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
    issue_cert_command = ['./acme.sh', '--issue', '-d', 'domain.com', '--dns', 
                            '--yes-I-know-dns-manual-mode-enough-go-ahead-please']
    renew_cert_command = ['./acme.sh', '--renew', '-d', 'domain.com', '--dns', 
                            '--yes-I-know-dns-manual-mode-enough-go-ahead-please']
    # test_acme_command = ['acme.sh','-v']
    # create_alias_command = [alias alias_name=’command’]
    def __init__(self,domain,verify):
        self.domain = domain
        self.issue_cert_command[3] = self.renew_cert_command[3] = self.domain
        self.verify =verify

    def run_commands(self,commands):
        process = subprocess.Popen(commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.wait() # Wait for process to complete.

        # iterate on the stdout line by line
        outputs = []
        for line in process.stdout.readlines():
            outputs.append(line.decode("utf-8"))

        # print("ERROR")

        errors_and_warnings = []
        for line in process.stderr.readlines():
            errors_and_warnings.append(line.decode("utf-8"))
        return outputs,errors_and_warnings
    
    def install_acme(self):
        out,warn_err = self.run_commands(self.clone_url_command)
        for err in warn_err:
            print(err)
        self.currdir = os.getcwd()
        os.chdir(os.path.join(self.currdir,"acme.sh"))

        print("upgrading...")
        out,warn_err = self.run_commands(self.upgrade_acme_command)
        print(out[-1])

        out, warn_err = self.run_commands(self.install_acme_command)
        for x in out:
            print(x)
            
    
    def issue_cert(self):
        pass

if __name__ == '__main__':
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('--d', action='store', type=str)
    my_parser.add_argument('--v', action='store', type=str)
    args = my_parser.parse_args()
    # print(vars(args))
    obj = SetupSSL(vars(args)['d'],vars(args)['v'])
    obj.install_acme()
    # print(obj.issue_cert_command)