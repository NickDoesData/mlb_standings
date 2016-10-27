def format_line_chart(df, colors, index=True, width=9,height=7,title='', subtitle='',note='', \
                              title_font_size=16,axis_font_size=13,legend_loc='', title_shift=0, note_shift=0, gridlines=''):
    
    import matplotlib.pyplot as plt  
    import numpy as np
    
    max_over = df.max().max()
    max_under = df.min().min()

    title_color = (21/255.,75/255.,119/255.)
     # Colors should be passed in a np.array .    
    

    # Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.   
    colors = colors/ 255.
   
    fig = plt.figure(figsize=(width, height))    

    # Remove the plot frame lines. They are unnecessary chartjunk.    
    #subplot 111 indicates no subplots
    ax = plt.subplot(111)    
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(True)    
    ax.spines["right"].set_visible(False)    
    ax.spines["left"].set_visible(True)    

    # Ensure that the axis ticks only show up on the bottom and left of the plot.    
    ax.get_xaxis().tick_bottom()    
    ax.get_yaxis().tick_left()    
  
    xmin = df.index.min()
    xmax = df.index.max()
 
    
    
    # Make sure your axis ticks are large enough to be easily read.    
    # You don't want your viewers squinting to read your plot.    
    plt.yticks(range(-40, 40, 20),  fontsize=14)    
    plt.xticks(range(20, 162, 20), fontsize=14)    
    
    ax.set_yticks([0], minor=True)    
    ax.yaxis.grid(True, which='minor', color='black', linestyle='-')

    plt.yticks(fontsize=14)
    
    plt.xlabel("game of season", fontsize=14)
    plt.ylabel("games over .500", fontsize=14)

    # Remove the tick marks; they are unnecessary with the tick lines we just plotted.    
    plt.tick_params(axis="both", which="both", bottom="on", top="off",    
                    labelbottom="on", left="on", right="off", labelleft="on", length=7, width=1.3)    

    cols = df.columns   

    for rank, column in enumerate(cols):    
        # Plot each line separately with its own color, using the Tableau 20    
        # color set in order.    
        plt.plot(df.index,    
                df[column].values,    
                lw=2.5, color=colors[rank])    

        # Add a text label to the right end of every line. Most of the code below    
        # is adding specific offsets y position because some labels overlapped.    
        y_pos = df[column].values[-1]
        x_pos = df.index.max() + 1  
  
        winning_pct = ("%.3f" % round(((df[column].values[-1] / 2 + 81 ) / 161.0),3)).lstrip('0')
        # Again, make sure that all labels are large enough to be easily read    
        # by the viewer.    
        plt.text(max(df.index) + 1, y_pos, column + ", " + str(winning_pct), fontsize=14, color=colors[rank])    



    # Note that if the title is descriptive enough, it is unnecessary to include        
    plt.text(np.median(df.index), max(ax.get_ylim()) + 5, title, fontsize=16, ha="center", style='normal')    


    if note <> '': 
        plt.text(min(df.index), min(ax.get_ylim())-5, note, fontsize=10)    
 

    return fig