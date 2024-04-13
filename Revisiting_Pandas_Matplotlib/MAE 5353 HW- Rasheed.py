# -*- coding: utf-8 -*-
"""
Name: Rasheed Shittu
Course:MAE 5353
Task: Homework 1-Module F
Description: This Python script is written to use Pandas to read in data and make a plot using Matplotlib

"""

# Importing Pandas and Matplotlib modules
import pandas as pd
from matplotlib import pyplot as plt

# creating the plotting function


def create_performance_plot(source_file, plot_fname, dpi=300):

    # Name of the columns which will be given to the data read in
    column_names = [
        "Ambient Temperature (°C)",
        "Ambient Temperature (°F)",
        "Ambient Temperature (K)",
        "EER (Btu/Wh)",
        "COP (W/W)"]

    # Reading in the data from xlsx file
    steady_state_df = pd.read_excel(
        source_file,
        sheet_name='SteadyState',
        skiprows=0,
        header=2,
        names=column_names)

    uncertainty_df = pd.read_excel(
        source_file,
        sheet_name='OverallUncertainties',
        skiprows=0,
        header=2,
        names=column_names)

    # Get the ambient temperature in Farenheint from the steady state dataframe
    # assigning primary x-axis values (ambient temp oF)
    T_amb_F = steady_state_df['Ambient Temperature (°F)']
    # Get the ambient temperature uncertainty values in Farenheint from the
    # uncertainty dataframe
    T_amb_err_F = uncertainty_df['Ambient Temperature (°F)']
    # Get the COP values in the COP column of the steady state dataframe
    COP = steady_state_df['COP (W/W)']
    # Get the COP uncertainty values in the COP column of the uncertainty
    # dataframe
    COP_err = uncertainty_df['COP (W/W)']

    # Create a figure and a subplot of COP vs ambient temperature in the
    # primary axis
    fig, ax1 = plt.subplots()

    # Create a scatter plot with error bar
    ax1.errorbar(
        T_amb_F,
        COP,
        xerr=T_amb_err_F,
        yerr=COP_err,
        c='tab:blue',
        fmt='s',
        ecolor='tab:blue',
        capthick=1,
        capsize=3,
        label='COP')

    # Create x and y axis label,legend and insert a grid
    ax1.set_xlabel('Ambient Temperature (°F)')
    ax1.set_ylabel('Coefficient of Performance (W/W)')
    ax1.legend()
    ax1.grid()

    # Create a secondary x-axis sharing y-axis with plot ax1
    ax2 = ax1.twiny()

    # Set the label
    ax2.set_xlabel('Ambient Temperature (°C)')

    # Setting the x-axis ticks label using the xaxis ticks label from ax1
    # plot, converting each one to degree Celcius
    ax2.set_xlim(ax1.get_xlim())
    ax2.set_xticks(ax1.get_xticks()[1:-1])
    ax2.set_xticklabels([f"{(f-32)/1.8:.1f}" for f in ax1.get_xticks()[1:-1]])

    # Create a second secondary x-axis sharing y-axis with plot ax1
    ax3 = ax1.twiny()

    # Set the position to the top of the plot and few distance away from the
    # exiting axis to avoid overlapping
    ax3.spines["top"].set_position(("axes", 1.2))

    # Setting the label
    ax3.set_xlabel('Ambient Temperature (K)')

    # Setting the x-axis ticks label using the xaxis ticks label from ax1
    # plot, converting each one to Kelvin
    ax3.set_xlim(ax1.get_xlim())
    ax3.set_xticks(ax1.get_xticks()[1:-1])
    # Converting the ticks label to Kelvin
    ax3.set_xticklabels(
        [f"{((f-32)/1.8)+273.15:.1f}" for f in ax1.get_xticks()[1:-1]])

    # Create a secondary y-axis sharing x-axis with plot ax1
    ax4 = ax1.twinx()
    # Set the label
    ax4.set_ylabel('Energy Efficiency Ratio (Btu/Wh)')

    # Setting the y-axis ticks label using the yaxis ticks label from ax1
    # plot, converting each one to EER in Btu/Wh
    ax4.set_ylim(ax1.get_ylim())
    ax4.set_yticks(ax1.get_yticks()[1:-1])
    # Setting the tick labels converting each one to Btu/Wh
    ax4.set_yticklabels([f"{f*3.41:.1f}" for f in ax1.get_yticks()[1:-1]])

    # Save the plot
    plt.savefig(plot_fname + ".png", dpi=dpi, bbox_inches='tight')
    plt.savefig(plot_fname + ".svg", bbox_inches='tight')
    # Show plot
    plt.show()


if __name__ == "__main__":
    # Run an example of the function
    source_file = "MAE_5353_VersionControl/Revisiting_Pandas_Matplotlib/PerformanceData_Unitxx_RasheedShittu.xlsx"
    plot_fname = "MAE_5353_VersionControl/Revisiting_Pandas_Matplotlib/MAE5353_HW"

    create_performance_plot(source_file, plot_fname, dpi=300)
