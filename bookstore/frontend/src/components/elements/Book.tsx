import React from "react";
import './Book.css'

import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import CloudDownloadIcon from '@material-ui/icons/CloudDownload';
import {IBook} from "../../shared/interfaces";


export function Book(props: IBook) {
    const {name, image, author} = props

    // @ts-ignore
    return(
        <Card className={'bookContainer'}>
            <CardActionArea>
                <CardMedia
                    className={'bookPicture'}
                    style={{objectFit: 'contain'}}
                    component="img"
                    // objectFit: 'cover'
                    alt="Contemplative Reptile"
                    image={image}
                    title="Contemplative Reptile"
                />
                <CardContent>
                    <Typography gutterBottom variant="h5" component="h2">
                        {name}
                    </Typography>
                    <Typography variant="body2" color="textSecondary" component="p">
                        {("Lizards are a" +
                            " widespread group of squamate" +
                        " reptiles, with over" +
                            " 6,000 species, ranging").slice(20)+ '...'}

                    </Typography>
                </CardContent>
            </CardActionArea>
            <CardActions>
                <Button startIcon={<CloudDownloadIcon />}
                    size="small" color="primary">
                    Download
                </Button>
                <Button size="small" color="primary">
                    Learn more
                </Button>
            </CardActions>
        </Card>

    )
}

