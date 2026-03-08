import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from XGRAV.constants import *

# Change to dark mode!
plt.style.use('dark_background')

def run(data, labels, frame_time, fps=30, limtype='square',zoom=1.0,save=''):
    
    # number of frames
    nframes = len(data)

    #number of bodies
    nbodies = len(data[0])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Calculate the limits of plot
    if limtype=='square':
        side = np.max(data[:,:,0])/zoom
        x_min, x_max = -side, +side
        y_min, y_max = -side, +side
        z_min, z_max = -side, +side

        
    else: 
        x_min, x_max = np.min(data[:,:,0]), np.max(data[:,:,0])
        y_min, y_max = np.min(data[:,:,1]), np.max(data[:,:,1])
        z_min, z_max = np.min(data[:,:,2]), np.max(data[:,:,2])
    
    # Add border padding
    padding_ratio = 0.1
    x_pad = (x_max-x_min)*padding_ratio
    y_pad = (y_max-y_min)*padding_ratio
    z_pad = (z_max-z_min)*padding_ratio

    # Set limits to the plot
    ax.set_xlim(xmin=x_min-x_pad, xmax=x_max+x_pad)
    ax.set_ylim(ymin=y_min-y_pad, ymax=y_max+y_pad)
    ax.set_zlim(zmin=z_min-z_pad, zmax=z_max+z_pad)

    # Axes and Grid
    ax.set_facecolor('#1a1a1a') # background for the plot area
    ax.tick_params(axis='x', colors='lightgray') # Gray ticks and labels
    ax.tick_params(axis='y', colors='lightgray')
    ax.set_xlabel('X Position (m)', color='lightgray') # Labels for clarity
    ax.set_ylabel('Y Position (m)', color='lightgray')
    ax.set_zlabel('Z Position (m)', color='lightgray')
    ax.set_title('N-Body Orbital Simulation', color='white', fontsize=16)

    # Remove the default grid for a cleaner look, or make it very subtle
    ax.grid(False) 
    # Or, if you want a subtle grid:
    # ax.grid(True, linestyle=':', alpha=0.3, color='gray')

    # Store all lines
    all_lines = []

    #Store all blob
    all_blobs = []
    
    # Make a vibrant color list
    colors = plt.cm.get_cmap('hsv', nbodies + 1) # A colormap for diverse colors

    # Add all bodie's lines and blobs to list
    for n in range(nbodies):
        
        body_color = colors(n / nbodies) # Get a color from the colormap

        line = ax.plot3D(data[0,n,0],
                        data[0,n,1],
                        data[0,n,2],
                        label=labels[n],
                        color=body_color,
                        linewidth=2,
                        alpha=0.5,
                        solid_capstyle='round')[0]

        blob = ax.scatter3D(data[0,n,0], 
                          data[0,n,1],
                          data[0,n,2],
                          s=75,
                          color=body_color,
                          edgecolor='white',
                          linewidth=0.5,
                          alpha=0.9)

        all_lines.append(line)
        all_blobs.append(blob)

    # Place legend
    ax.legend(
        loc='upper right', 
        facecolor='#2a2a2a', # Dark background for legend
        edgecolor='none',    # No border
        fontsize='medium', 
        labelcolor='white')
    
    # Timer Text
    # ax.transAxes to position it relative to the plot (0,0 is bottom-left, 1,1 is top-right)
    timer_text = ax.text2D(
        0.02, 0.98,          # Position
        "Time: 0.0 Years",    # Initial text
        color='white',       # Text color
        fontsize=12,
        fontweight='bold',   # style
        ha='left',           # Horizontal alignment
        va='top',            # Vertical alignment
        transform=ax.transAxes # Positions relative to the axes, not data
    )

    # Define updateFrame function
    def updateFrame(frame):

        # Calculate the time
        current_time_sec = frame * frame_time
        current_time_years = current_time_sec / SECONDS_PER_YEAR

        # Update the timer text
        timer_text.set_text(f"Time: {current_time_years:.2f} Year")


        # Update positions for each body
        for n in range(nbodies):
            
            # Get the line and blob of the body
            line = all_lines[n]
            blob = all_blobs[n]

            xarr = data[:frame+1, n, 0]
            yarr = data[:frame+1, n, 1]
            zarr = data[:frame+1, n, 2]
            
            xpos = data[frame, n, 0]
            ypos = data[frame, n, 1]
            zpos = data[frame, n, 2]


            line.set_data(xarr,yarr)
            line.set_3d_properties(zarr)

            blob._offsets3d = ([xpos], [ypos], [zpos])

        return *all_lines, *all_blobs, timer_text
    
    interval = 1000/fps

    # Make the animation variable
    anim = animation.FuncAnimation(fig, updateFrame, frames=nframes, interval=interval)

    # Save the file if save=True
    if len(save) != 0:
        print('Saving the animation...')
        anim.save(f'Animations/{save}', dpi=150)
        print('Animation Saved!')
    # Display the animation
    plt.show()



def run_sidebyside(data, labels, frame_time, fps=30, center=0,limtype='square',zoom=1.0,save=''):

    # number of frames
    nframes = len(data)

    #number of bodies
    nbodies = len(data[0])

    # define center

    fig = plt.figure(figsize=(12, 10))
    ax_main = fig.add_subplot(121, projection='3d')
    ax_zoom = fig.add_subplot(122, projection='3d')

    all_lines_main = []
    all_lines_zoom = []
    all_blobs_main = []
    all_blobs_zoom = []

    colors = plt.cm.get_cmap('hsv', nbodies + 1) # A colormap for diverse colors

    for n in range(nbodies):

        body_color = colors(n / nbodies) # Get a color from the colormap

        line_main = ax_main.plot3D(data[0,n,0],
                                   data[0,n,1],
                                   data[0,n,2],
                                   label=labels[n],
                                   color=body_color,
                                   linewidth=2,
                                   alpha=0.5,
                                   solid_capstyle='round')[0]
        
        blob_main = ax_main.scatter3D(data[0,n,0], 
                          data[0,n,1],
                          data[0,n,2],
                          s=75,
                          color=body_color,
                          edgecolor='white',
                          linewidth=0.5,
                          alpha=0.9)
        
        all_lines_main.append(line_main)
        all_blobs_main.append(blob_main)

        line_zoom = ax_zoom.plot3D(data[0,n,0],
                                   data[0,n,1],
                                   data[0,n,2],
                                   label=labels[n],
                                   color=body_color,
                                   linewidth=2,
                                   alpha=0.5,
                                   solid_capstyle='round')[0]
        
        blob_zoom = ax_zoom.scatter3D(data[0,n,0], 
                          data[0,n,1],
                          data[0,n,2],
                          s=75,
                          color=body_color,
                          edgecolor='white',
                          linewidth=0.5,
                          alpha=0.9)
        
        all_lines_zoom.append(line_zoom)
        all_blobs_zoom.append(blob_zoom)

    # Find the full data range for all axes
    x_min, x_max = np.min(data[0,:,0]), np.max(data[0,:,0])
    y_min, y_max = np.min(data[0,:,1]), np.max(data[0,:,1])
    z_min, z_max = np.min(data[0,:,2]), np.max(data[0,:,2])

    # Find the center point of the simulation 
    x_center = data[0,center,0]
    y_center = data[0,center,1]
    z_center = data[0,center,2]

    # Find the largest range
    max_range = np.max([x_max - x_min, y_max - y_min, z_max - z_min])
    
    # Add a padding 
    plot_radius = (max_range / 2.0) * 1.1 

    # Set UNIFORM limits for the main plot
    ax_main.set_xlim(x_center - plot_radius, x_center + plot_radius)
    ax_main.set_ylim(y_center - plot_radius, y_center + plot_radius)
    ax_main.set_zlim(z_center - plot_radius, z_center + plot_radius)

    # Set UNIFORM limits for the zoom plot ---
    zoom_plot_radius = plot_radius / zoom 

    ax_zoom.set_xlim(x_center - zoom_plot_radius, x_center + zoom_plot_radius)
    ax_zoom.set_ylim(y_center - zoom_plot_radius, y_center + zoom_plot_radius)
    ax_zoom.set_zlim(z_center - zoom_plot_radius, z_center + zoom_plot_radius)

    ax_main.legend(
        loc='upper right', 
        facecolor='#2a2a2a', # Dark background for legend
        edgecolor='none',    # No border
        fontsize='medium', 
        labelcolor='white')

    timer_text = ax_main.text2D(
        0.02, 0.98,          # Position
        "Time: 0.0 Years",    # Initial text
        color='white',       # Text color
        fontsize=12,
        fontweight='bold',   # A bit of style
        ha='left',           # Horizontal alignment
        va='top',            # Vertical alignment
        transform=ax_main.transAxes # Positions relative to the axes, not data
    )

    zoom_text = ax_zoom.text2D(
        0.02, 0.98,          # Position
        f"Zoom : {zoom}x",    # Initial text
        color='white',       # Text color
        fontsize=12,
        fontweight='bold',   # A bit of style
        ha='left',           # Horizontal alignment
        va='top',            # Vertical alignment
        transform=ax_zoom.transAxes)

    def updateFrame(frame):

        # Calculate the time
        current_time_sec = frame * frame_time
        current_time_years = current_time_sec / SECONDS_PER_YEAR

        # Update the timer text
        timer_text.set_text(f"Time: {current_time_years:.2f} Year")


        # Update positions for each body
        for n in range(nbodies):
            
            # Get the line and blob of the body
            line_main = all_lines_main[n]
            blob_main = all_blobs_main[n]

            line_zoom = all_lines_zoom[n]
            blob_zoom = all_blobs_zoom[n]

            xarr = data[:frame+1, n, 0]
            yarr = data[:frame+1, n, 1]
            zarr = data[:frame+1, n, 2]
            
            xpos = data[frame, n, 0]
            ypos = data[frame, n, 1]
            zpos = data[frame, n, 2]


            line_zoom.set_data(xarr,yarr)
            line_zoom.set_3d_properties(zarr)

            line_main.set_data(xarr,yarr)
            line_main.set_3d_properties(zarr)

            blob_main._offsets3d = ([xpos], [ypos], [zpos])
            blob_zoom._offsets3d = ([xpos], [ypos], [zpos])

        x_min, x_max = np.min(data[frame,:,0]), np.max(data[frame,:,0])
        y_min, y_max = np.min(data[frame,:,1]), np.max(data[frame,:,1])
        z_min, z_max = np.min(data[frame,:,2]), np.max(data[frame,:,2])

        max_range = np.max([x_max - x_min, y_max - y_min, z_max - z_min])
        plot_radius = (max_range / 2.0) * 1.1 
        zoom_plot_radius = plot_radius / zoom 
        
        x_center = data[frame,center,0]
        y_center = data[frame,center,1]
        z_center = data[frame,center,2]


        ax_zoom.set_xlim(x_center - zoom_plot_radius, x_center + zoom_plot_radius)
        ax_zoom.set_ylim(y_center - zoom_plot_radius, y_center + zoom_plot_radius)
        ax_zoom.set_zlim(z_center - zoom_plot_radius, z_center + zoom_plot_radius)

        ax_main.set_xlim(x_center - plot_radius, x_center + plot_radius)
        ax_main.set_ylim(y_center - plot_radius, y_center + plot_radius)
        ax_main.set_zlim(z_center - plot_radius, z_center + plot_radius)

        return *all_lines_main, *all_blobs_main, *all_lines_zoom, *all_blobs_zoom, timer_text
    

    interval = 1000/fps

    # Make the animation variable
    anim = animation.FuncAnimation(fig, updateFrame, frames=nframes, interval=interval)

    # Save the file if save=True
    if len(save) != 0:
        print('Saving the animation...')
        anim.save(f'Animations/{save}', dpi=150)
        print('Saved!')
    # Display the animation
    plt.show()
