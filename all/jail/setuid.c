#include <unistd.h>
int main()
{
    setreuid(1000,1000);
    execl("/bin/bash", "bash", (char *)NULL);
    return 0;
}
