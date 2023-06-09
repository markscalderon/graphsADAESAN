#include <iostream>
#include "Graph.h"
using namespace std;

int main()
{
    Graph* G = new Graph();
    G->load_from_file("largeG.txt");
    //G->show();
    return 0;
}
