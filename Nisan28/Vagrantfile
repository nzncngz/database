#  with access, by name, to other vms
Vagrant.configure(2) do |config|
  config.vm.define "database", primary: true do |h|
    h.vm.box = "centos/7"
    h.vm.hostname =  "database"
    h.vm.network "private_network", ip: "192.168.135.148"
    h.vm.network "forwarded_port", guest: 22, host: "2200", id: "ssh"
    h.vm.provision :shell, inline: "echo 'export ANSIBLE_CONFIG=/vagrant/ansible/ansible.cfg' >> /home/vagrant/.bash_profile"
    #h.vm.provision "shell" do |provision|
    #  provision.path = "provision_ansible.sh"
    #end 
    h.vm.provision :shell, :inline => <<'EOF'
	if [ ! -f "/home/vagrant/.ssh/id_rsa" ]; then
  ssh-keygen -t rsa -N "" -f /home/vagrant/.ssh/id_rsa
fi
cp /home/vagrant/.ssh/id_rsa.pub /vagrant/control.pub
cat << 'SSHEOF' > /home/vagrant/.ssh/config
Host *
  StrictHostKeyChecking no
  UserKnownHostsFile=/dev/null
SSHEOF
chown -R vagrant:vagrant /home/vagrant/.ssh/
EOF
  end

end
