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


void win() {
    asm("andq $-16, %rsp");

    char flag[69] = {0};
    int fd = open("flag.txt", O_RDONLY);
    if (fd == -1) {
        perror("open failed");
    }

    read(fd, flag, 69);
    puts(flag);
}

void vuln() {
    char buf[8] = {0};

    gets(buf);
    puts(buf);
}

int main() {
    upkeep();
    vuln();
}
