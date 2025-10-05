# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "debian/bookworm64"

  config.vm.network "forwarded_port", guest: 5000, host: 5000

  config.vm.provision "file", source: "hello.py", destination: "/home/vagrant/hello.py"

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    
    apt-get install -y python3 python3-pip python3-venv
    
    cd /home/vagrant
    sudo -u vagrant python3 -m venv venv
    
    sudo -u vagrant /home/vagrant/venv/bin/pip install Flask
    
    cat > /etc/systemd/system/flask.service <<'EOF'
[Unit]
Description=Flask Application
After=network.target

[Service]
User=vagrant
WorkingDirectory=/home/vagrant
Environment="PATH=/home/vagrant/venv/bin"
ExecStart=/home/vagrant/venv/bin/flask --app hello run --host=0.0.0.0
Restart=always

[Install]
WantedBy=multi-user.target
EOF

    systemctl daemon-reload
    systemctl enable flask
    systemctl start flask
  SHELL
end