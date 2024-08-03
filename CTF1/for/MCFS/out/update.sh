mvn clean package
jar -uf target/mcfs-1.jar plugin.yml
cp target/mcfs-1.jar ../server/plugins/mcfs.jar
