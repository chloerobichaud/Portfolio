@interact
def interactive_plot(neuron=neuron_labels):
    fig = plt.figure(figsize=[20, 15])

    neu_dat = df[(df['neuron'] == neuron)]

    subplot_counter = 1
    for contr in contr_labels:
        tmp_dat = neu_dat[(neu_dat['contrast'] == contr)]

        for cond in cond_labels:
            ax = fig.add_subplot(len(contr_labels), len(cond_labels), subplot_counter)
            for rep in rep_labels:
                spike_times = \
                tmp_dat[(tmp_dat['condition'] == cond) & (tmp_dat['repetition'] == rep) & (tmp_dat['spike'] == 1)][
                    'time']
                plt.vlines(spike_times, rep, rep + 1, color='black', linestyle='--', linewidth=.75)
            if cond == 'ADAPT':
                plt.axvspan(0, stim_on_time - 1, alpha=0.5, color='grey')

            plt.axvspan(stim_on_time, stim_off_time, alpha=contr / 100, color='grey')

            plt.xlim([0, max(time_labels) + 1])
            plt.ylim([0, len(rep_labels)])
            plt.title(cond + ' ' + str(contr) + '% contrast')
            plt.xlabel('Time (ms)')
            plt.ylabel('Repetition', )
            plt.yticks([x + 0.5 for x in range(num_reps)], [str(x + 1) for x in range(num_reps)], size=8)
            plt.tight_layout()
            subplot_counter += 1


plt.show()