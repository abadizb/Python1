import searcher
import data_load
import indexer
import quotes



indexer.indexer()
searcher.searcher()
data_load.traverser()

d = indexer.indexer("raw_data.pickle")
searcher.search(d)
