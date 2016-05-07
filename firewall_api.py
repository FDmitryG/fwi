import subprocess

PIPE = subprocess.PIPE


class FireWall:
    @staticmethod
    def get_chains():
        cmd = "sudo iptables -vL | grep Chain | cut -d \  -f2"
        cmd_stdout = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, close_fds=True)
        line = str(cmd_stdout.stdout.read(), "utf-8")
        chains = line.splitlines()
        return chains

    def get_chain_data(self, chain):
        full_output = subprocess.check_output(["sudo", "iptables", "-vL", "{}".format(chain), "--line-number"],
                                              universal_newlines=True)
        lines = full_output.splitlines()
        chain_name = lines[0]
        row = []
        for i in range(2, len(lines)):
            row.append(' '.join(lines[i].split()).split(" "))
        return chain_name, row

    def get_help(self):
        ipt_help = subprocess.check_output(["sudo", "iptables", "-h"], universal_newlines=True)
        return ipt_help

    def add_rule(self, chain, new_rule_rs, new_rule_prot, new_rule_dport, new_rule_address, new_rule_action):
        chain = chain
        new_rule_rs = new_rule_rs
        new_rule_prot = new_rule_prot
        new_rule_dport = new_rule_dport
        new_rule_address = new_rule_address
        new_rule_action = new_rule_action

        if new_rule_dport and new_rule_address:
            cmd = "sudo iptables -{rs} {chain} -p {prot} --dport \
            {dport} -s {address} -j {action}".format(rs=new_rule_rs, chain=chain, prot=new_rule_prot,
                                                     dport=new_rule_dport, address=new_rule_address,
                                                     action=new_rule_action)
        elif new_rule_dport and not new_rule_address:
            cmd = "sudo iptables -{rs} {chain} -p {prot} --dport \
            {dport} -j {action}".format(rs=new_rule_rs, chain=chain, prot=new_rule_prot,
                                        dport=new_rule_dport, action=new_rule_action)
        elif not new_rule_dport and new_rule_address:
            cmd = "sudo iptables -{rs} {chain} -p {prot} \
            -s {address} -j {action}".format(rs=new_rule_rs, chain=chain, prot=new_rule_prot,
                                             address=new_rule_address, action=new_rule_action)
        else:
            cmd = "sudo iptables -{rs} {chain} -p {prot} -j {action}".format(rs=new_rule_rs, chain=chain,
                                                                             prot=new_rule_prot,
                                                                             action=new_rule_action)

        subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, close_fds=True)

    def del_rule(self, chain, rul_number):
        chain = chain
        rule = rul_number
        cmd = "sudo iptables -D {} {}".format(chain, rule)
        subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, close_fds=True)

    def add_chain(self, new_chain_name):
        cmd = "sudo iptables -N {}".format(new_chain_name)
        subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, close_fds=True)

    def del_chain(self, del_chain_name):
        cmd = "sudo iptables -X {}".format(del_chain_name)
        subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, close_fds=True)

    def export_conf(self):
        chains = self.get_chains()
        with open('iptables.conf', 'w') as file:
            for chain in chains:
                chains_data = self.get_chain_data(chain)
                full_data = chains_data[1]
                if full_data != []:
                    file.write("# {} \n".format(chain))
                for lines in full_data:
                    lines = ' '.join(lines)
                    file.write("{} \n".format(lines))

if __name__ == '__main__':
    # action = FireWall()
    # print(action.get_chain_data("INPUT"))
    # action.export_conf()
    pass


