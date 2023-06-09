#include "Graph.h"
#include <iostream>
#include <fstream>
using namespace std;
Graph::Graph()
{
    this->E = 0;
    this->V = 0;
}

Graph::~Graph()
{

}
void Graph::load_from_file(string path){
    ifstream file;
    file.open(path);
    if(file.fail())
        return;

    file>>this->V;
    file>>this->E;
    for(int i=0;i<this->V; i++){
        this->adj.push_back(vector<int>());
    }
    int v,w;
    for(int j=0;j<this->E;j++){
        file>>v>>w;
        addEdge(v,w);
    }
}
void Graph::addEdge(int v, int w){
    if (validateVertex(v) && validateVertex(w)){
        this->adj[v].push_back(w);
        this->adj[w].push_back(v);
    }
}
bool Graph::validateVertex(int v){
    if (v < 0 && v>this->V)
        return false;
    else
        return true;
}
void Graph::show(){
    for(int i=0;i<this->getV();i++){
        cout<<i<<": ";
        for(auto num: this->getAdj(i)){
            cout<<num<<" ";
        }
        cout<<endl;
    }
}
