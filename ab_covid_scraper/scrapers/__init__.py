from ab_covid_scraper.scrapers.ahs_heatmap import AlbertaHealthServiceHeatmapScraper
from ab_covid_scraper.scrapers.manager import ScraperManager

ScraperManager.add_scraper(AlbertaHealthServiceHeatmapScraper)