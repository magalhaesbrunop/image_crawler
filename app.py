from icrawler.builtin import GoogleImageCrawler


number_images_collected = 20
name_image = 'torresmo'
number_feeder_threads = number_images_collected
file_image = name_image

# Numero de carregamento e analise das imagens e o local de salvamento
google_crawler = GoogleImageCrawler(
    feeder_threads = number_images_collected,
    parser_threads = 200,
    storage={'root_dir': file_image}
    )

# Uso dos filtros conforme a interface do Google imagens
filters = dict(
    size= "large"
)

# Nome e a quantidade de imagens a serem buscadas
google_crawler.crawl(keyword=name_image, max_num=number_feeder_threads)