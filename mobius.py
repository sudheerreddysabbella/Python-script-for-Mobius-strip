#import dependencies
import numpy as np
import plotly.graph_objects as go

#Mobius strip class
class MobiusStrip:
    """
    A class to represent a Mobius strip and compute its surface area and edge length.
    """
    def __init__(self, R=1.0, w=0.3, n=200):
        """
        Initialize the Mobius strip with:
        R: radius of the central circle
        w: width of the strip
        n: resolution (number of points for u and v)
        """
        self.R = R
        self.w = w
        self.n = n
        # Generate 'n' evenly spaced values from 0 to 2π, representing the angular parameter 'u'
        self.u = np.linspace(0, 2 * np.pi, n)
        # Generate 'n' evenly spaced values from -w/2 to w/2, representing the vertical parameter 'v'
        self.v = np.linspace(-w/2, w/2, n)
        # Generate 2D coordinate grids from the 1D arrays self.u and self.v for parameterization
        self.u_grid, self.v_grid = np.meshgrid(self.u, self.v)
        # Generate the 3D mesh coordinates (X, Y, Z) based on the parameter grids using the mesh generation method
        self.X, self.Y, self.Z = self.generate_mesh()

    def generate_mesh(self):
        """
        Generate a 3D mesh using parametric equations.
        """
        u, v = self.u_grid, self.v_grid
        # Calculate the radius offset to avoid double computation
        radius_offset = self.R + v * np.cos(u / 2)
        X = radius_offset * np.cos(u)  # (R + v * cos(u/2)) * cos(u)
        Y = radius_offset * np.sin(u)  # (R + v * cos(u/2)) * sin(u)
        Z = v * np.sin(u/2)
        return X, Y, Z

    def compute_surface_area(self, fix=14):
        """
        Approximate the surface area using numerical integration.
        A ≈ ∬ ||∂r/∂u × ∂r/∂v|| du dv
        """
        u, v = self.u_grid, self.v_grid
        du = self.u[1] - self.u[0]
        dv = self.v[1] - self.v[0]
        
        # Precompute common terms
        cos_u = np.cos(u)
        sin_u = np.sin(u)
        cos_u_half = np.cos(u/2)
        sin_u_half = np.sin(u/2)
        # Partial derivatives
        dx_du = -sin_u * (self.R + v * cos_u_half) - 0.5 * v * sin_u_half * cos_u  # -sin(u) * (R + v * cos(u/2)) - 0.5 * v * sin(u/2) * cos(u)
        dy_du =  cos_u * (self.R + v * cos_u_half) - 0.5 * v * sin_u_half * sin_u  #  cos(u) * (R + v * cos(u/2)) - 0.5 * v * sin(u/2) * sin(u)
        dz_du =  0.5 * v * cos_u_half

        dx_dv = cos_u_half * cos_u
        dy_dv = cos_u_half * sin_u
        dz_dv = sin_u_half

        # Cross product magnitude ||∂r/∂u × ∂r/∂v||
        cross_mag = np.sqrt(
            (dy_du * dz_dv - dz_du * dy_dv)**2 +
            (dz_du * dx_dv - dx_du * dz_dv)**2 +
            (dx_du * dy_dv - dy_du * dx_dv)**2
        )

        surface_area = np.sum(cross_mag) * du * dv
        return round(surface_area, fix)

    def compute_edge_length(self, fix=14):
        """
        Approximate the edge length by tracing v = ±w/2 (top & bottom edges).
        """
        u = self.u
        v_edge = self.w/2
        adj_R = self.R + v_edge * np.cos(u/2)  # Calculate the adjusted radius to avoid multiple identical computation
        # Top edge (v = +w/2)
        x1 = adj_R * np.cos(u)
        y1 = adj_R * np.sin(u)
        z1 = v_edge * np.sin(u / 2)
        # Bottom edge (v = -w/2) — same path in reverse due to Möbius twist
        x2 = adj_R * np.cos(u)
        y2 = adj_R * np.sin(u)
        z2 = -v_edge * np.sin(u/2)

        # Combine the edge into one continuous path
        x = np.concatenate([x1, x2[::-1]])
        y = np.concatenate([y1, y2[::-1]])
        z = np.concatenate([z1, z2[::-1]])

        dx = np.diff(x)
        dy = np.diff(y)
        dz = np.diff(z)

        edge_length = np.sum(np.sqrt(dx**2 + dy**2 + dz**2))
        return round(edge_length, fix)

    def plot(self, color='Greys'):
        """
        Display an interactive 3D Möbius strip using Plotly.
        """
        fig = go.Figure(data=[go.Surface(
            x=self.X,
            y=self.Y,
            z=self.Z,
            colorscale=color,
            showscale=False,
            lighting=dict(ambient=0.6, diffuse=0.8),
            opacity=0.9
        )])

        fig.update_layout(
            title="Interactive 3D Möbius Strip",
            scene=dict(
                xaxis_title='X',
                yaxis_title='Y',
                zaxis_title='Z',
                aspectmode='data'
            ),
            margin=dict(l=30, r=30, b=30, t=60),
        )
        fig.show()

if __name__ == '__main__':
    #using the class
    strip = MobiusStrip(R=1.0, w=0.4, n=150)
    strip.plot()  # accept 87 diff gradient color scheme thorugh color parameter, refer the readme.md
    print("Surface Area:", strip.compute_surface_area())  # use fix parameter to fix the decimals count, for example fix=6 => result {x.xxxxxx}
    print("Edge Length:", strip.compute_edge_length())  # use fix parameter to round the decimal, for example fix=4 => result {x.xxxx}
    # by default fix is 14 and color is Greys
