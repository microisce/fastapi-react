import React from "react";
import './Header.css';

// import IconButton from "@material-ui/core/IconButton";
import Typography from "@material-ui/core/Typography";


import { makeStyles } from '@material-ui/core/styles';
import {Button} from "@material-ui/core";

export function Header() {
    const classes = useStyles();
    return(
        <div className={'mainBar'}>
            <div className={'topBar'}>
            <div className={'centered'}>
                <Button variant ='outlined' color="inherit">Subscribe</Button>
            </div>
            <div className={'centered'}>
                <Typography variant="h6" className={classes.title}>
                    Online BookStore
                </Typography>
            </div>
            <div className={'centered'}>
                <Button variant ='outlined' color="inherit">Login</Button>
            </div>


        </div>
        </div>
    )
}
const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
    },
    menuButton: {
        marginRight: theme.spacing(2),
    },
    title: {
        flexGrow: 1,
    }
}));
