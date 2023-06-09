#ifndef GRAPH_H
#define GRAPH_H
#include <vector>
#include <string>
using namespace std;

class Graph
{
    public:
        Graph();
        void load_from_file(string path);
        void addEdge(int v, int w);
        bool validateVertex(int v);
        int getV(){return this->V;};
        int getE(){return this->E;};
        vector<int> getAdj(int v){return this->adj[v];};

        int degree(int v){return this->adj[v].size();}
        virtual ~Graph();
        void show();
    private:
        int V;
        int E;
        vector<vector<int> > adj;
};

#endif // GRAPH_H
