import searcher
import data_load
import indexer
import quotes
import traverser

traverser.traverser()
indexer.indexer()
searcher.searcher()
data_load.get_traversal_data()

d = indexer.indexer("raw_data.pickle")
searcher.search(d)
