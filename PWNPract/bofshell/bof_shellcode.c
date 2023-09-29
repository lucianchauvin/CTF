#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

void upkeep() {
    // Not part of the challenge, ignore this
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}

void vuln() {
    char buf[128] = {0};
    printf("buf is at %p\n", buf);

    gets(buf);
    puts(buf);
}

int main() {
    upkeep();
    vuln();
}
