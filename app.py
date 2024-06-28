import click

from HttpClient.httpClient import ExchangeClient


@click.command()
@click.option("--currency", default="Dolar", help="Öğrenmek istediğiniz exchange adını giriniz")
def cli(exchange):
    client = ExchangeClient()
    try:
        print(client.scrape_exchange_rate(exchange))
    except Exception as e:
        print(e)