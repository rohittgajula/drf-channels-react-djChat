import { AppBar, Toolbar, Typography } from "@mui/material";
import { useTheme } from "@mui/material/styles";
import { Link } from "react-router-dom";

export const PrimaryAppBar = () => {
    const theme = useTheme();
    return (
        <AppBar
            sx={{
                backgroundColor: theme.palette.background.default,
                borderBottem: `1px solid ${theme.palette.divider}`,
            }}
        >
            <Toolbar variant="dense"
                sx={{
                    height: theme.primaryAppBar.height,
                    minHeight: theme.primaryAppBar.height,
                }}
            >
                <Link href="/" underline="none" color="inherit">
                    <Typography variant="h6" noWrap component="div" sx={{ display: { fontWeight: 700, letterSacing: "-0.5px" } }}>
                        rohit
                    </Typography>
                </Link>
            </Toolbar>
        </AppBar>
    );
};
