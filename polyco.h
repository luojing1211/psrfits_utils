
#ifndef _POLYCO_H
#define _POLYCO_H

#include <stdio.h>
#include <stdlib.h>

struct polyco {
    char psr[15];
    int mjd;
    double fmjd;
    double rphase;
    double f0;
    int nsite;
    int nmin;
    int nc;
    float rf;
    int used;
    double c[15];
};

int read_one_pc(FILE *f, struct polyco *pc);
int read_pc(FILE *f, struct polyco *pc, const char *psr, int mjd, double fmjd);
int read_all_pc(FILE *f, struct polyco **pc);
int select_pc(const struct polyco *pc, int npc, const char *psr,
        int imjd, double fmjd);
double psr_phase(const struct polyco *pc, int mjd, double fmjd, double *freq);
double psr_fdot(const struct polyco *pc, int mjd, double fmjd, double *fdot);
double psr_phase_avg(const struct polyco *pc, int mjd, 
        double fmjd1, double fmjd2);
int pc_range_check(const struct polyco *pc, int mjd, double fmjd);
int pc_out_of_range(const struct polyco *pc, int mjd, double fmjd);
int polycos_differ(const struct polyco *pc1, const struct polyco *pc2);

#include "psrfits.h"
int make_polycos(const char *parfile, struct hdrinfo *hdr, char *src, 
        struct polyco **pc);

#endif
