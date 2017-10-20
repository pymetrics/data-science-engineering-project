import click
from utils.parsing import parse_options

@click.group()
def main():
    """
    pymatrix: A command line tool for working with matrices.
    """
    pass


@click.command()
@click.argument('n', type=click.INT)
@click.option('-j', '--json-data', type=click.STRING,
              help='input matrix as a valid json object')
@click.option('-f', '--csv-file', type=click.Path(exists=True),
              help='read matrix from a csv file')
@click.option('-p', '--pickle-file', type=click.Path(exists=True),
              help='read matrix from a pickle file')
@click.option('-s', '--sparse-coo', type=click.Path(exists=True),
              help='read matrix in COO format from a file')
def echo(n, **kwargs):
    """
    Display the passed options N times
    """

    input_type, value = parse_options(**kwargs)

    for _ in range(n):
        click.echo(
            "\nThe given input was of type: %s\n"
            "And the value was: %s\n"
            %(input_type, value) 
        )


@click.command()
@click.argument('row_i', type=click.INT)
@click.option('-j', '--json-data', type=click.STRING,
              help='input matrix as a valid json object')
@click.option('-f', '--csv-file', type=click.Path(exists=True),
              help='read matrix from a csv file')
@click.option('-p', '--pickle-file', type=click.Path(exists=True),
              help='read matrix from a pickle file')
@click.option('-s', '--sparse-coo', type=click.Path(exists=True),
              help='read matrix in COO format from a file')
@click.option('--distance', default=False, type=click.BOOL, is_flag=True,
              help='print the distance between the pair of rows')
def closest_to(row_i, **kwargs):
    """
    Find the row that is the minimal distance from row_i and
    optionally display the distance as well

    Output Format:\n
      i j [d_ij]
    """
    pass


@click.command()
@click.argument('n', type=click.INT)
@click.option('-j', '--json-data', type=click.STRING,
              help='input matrix as a valid json object')
@click.option('-f', '--csv-file', type=click.Path(exists=True),
              help='read matrix from a csv file')
@click.option('-p', '--pickle-file', type=click.Path(exists=True),
              help='read matrix from a pickle file')
@click.option('-s', '--sparse-coo', type=click.Path(exists=True),
              help='read matrix in COO format from a file')
@click.option('--distance', default=False, type=click.BOOL, is_flag=True,
              help='print the distance between the pair of rows')
def closest(n, **kwargs):
    """
    Find the N distinct pairs of rows that are the smallest distance
    apart and optionally display the distance as well

    Output Format:\n
      i j [d_ij]
    """
    pass


@click.command()
@click.argument('n', type=click.INT)
@click.option('-j', '--json-data', type=click.STRING,
              help='input matrix as a valid json object')
@click.option('-f', '--csv-file', type=click.Path(exists=True),
              help='read matrix from a csv file')
@click.option('-p', '--pickle-file', type=click.Path(exists=True),
              help='read matrix from a pickle file')
@click.option('-s', '--sparse-coo', type=click.Path(exists=True),
              help='read matrix in COO format from a file')
@click.option('--distance', default=False, type=click.BOOL, is_flag=True,
              help='print the distance between the pair of rows')
def furthest(n, **kwargs):
    """
    Find the N distinct pairs of rows that are the furthest distance
    apart and optionally display the distance as well

    Output Format:\n
      i j [d_ij]
    """
    pass


@click.command()
@click.argument('n_centroids', type=click.INT)
@click.option('-j', '--json-data', type=click.STRING,
              help='input matrix as a valid json object')
@click.option('-f', '--csv-file', type=click.Path(exists=True),
              help='read matrix from a csv file')
@click.option('-p', '--pickle-file', type=click.Path(exists=True),
              help='read matrix from a pickle file')
@click.option('-s', '--sparse-coo', type=click.Path(exists=True),
              help='read matrix in COO format from a file')
def centroids(n_centroids, **kwargs):
    """
    Cluster the given data set and return the N centroids,
    one for each cluster
    """
    pass


main.add_command(echo)
main.add_command(closest_to)
main.add_command(closest)
main.add_command(furthest)
main.add_command(centroids)
