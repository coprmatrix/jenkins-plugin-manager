Name: jenkins-plugin-manager
Version: 0
Release: 0
License: MIT
URL: https://github.com/jenkinsci/plugin-installation-manager-tool
Source0: https://github.com/jenkinsci/plugin-installation-manager-tool/releases/download/%{version}/jenkins-plugin-manager-%{version}.jar
Summary: Plugin Manager CLI tool for Jenkins
BuildRequires: rpm_macro(_javadir)
Requires: java
BuildArch: noarch

%description
The plugin manager downloads plugins and their dependencies into a folder so that they can be easily imported into an instance of Jenkins. The goal of this tool is to replace the Docker install-plugins.sh script and the many other implementations of plugin management that have been recreated across Jenkins. The tool also allows users to see more information about the plugins they are downloading, such as available updates and security warnings. By default, plugins will be downloaded; the user can specify not to download plugins using the --no-download option.

%install
install -D "%{SOURCE0}" %{buildroot}%{_javadir}/jenkins-plugin-manager.jar
mkdir -p %{buildroot}%{_bindir}
cat << EOF > %{buildroot}%{_bindir}/jenkins-plugin-manager
#!/bin/sh
java -jar %{_javadir}/jenkins-plugin-manager.jar "${@}"
EOF

%files
%attr(0644, -, -) %{_javadir}/jenkins-plugin-manager.jar
%attr(0755, -, -) %{_bindir}/jenkins-plugin-manager

