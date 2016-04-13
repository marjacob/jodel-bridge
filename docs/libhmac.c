int Java_com_jodelapp_jodelandroidv3_api_HmacInterceptor_generate() {
    stack[2044] = ebx;
    sub_4d0();
    esi = stack[2044];
    ebp = (*(*esi + 0x2a4))(esi, stack[2044], 0x0);
    (*(*esi + 0x29c))(esi, client_secret());
    (*(*esi + 0x2a8))(esi, esi, ebp);
    eax = esi;
    return eax;
}

int client_secret() {
    stack[2046] = edi;
    stack[2045] = esi;
    stack[2044] = ebx;
    sub_4d0();
    get_generated_key();
    sub_410();
    edx = 0x0;
    do {
            edi = SAR(edx, 0x2);
            esi = !edx;
            edx = edx + 0x1;
            *(int8_t *)((esi & 0x3) + 0x29 + edi * 0x4) = *(0x29 + edi * 0x4) >> (esi & 0x3) * 0x8;
    } while (edx != 0x28);
    eax = 0x29;
    *(int8_t *)(eax + 0x28) = 0x0;
    return eax;
}

int get_generated_key() {
    stack[2047] = esi;
    stack[2046] = ebx;
    sub_4d0();
    ebx = ebx + 0x1abd;
    eax = get_random_key();
    edx = 0x0;
    esi = stack[2046];
    do {
            *(int8_t *)(edx + ebx + 0x7c) = *(int8_t *)(eax + edx) & 0xff ^ *(int8_t *)(esi + edx);
            edx = edx + 0x1;
    } while (edx != 0x28);
    eax = ebx + 0x7c;
    return eax;
}

int EntryPoint() {
    sub_4d0();
    eax = sub_400();
    return eax;
}

void sub_400() {
    (*(ebx + 0x14))();
    return;
}

void sub_410() {
    (*(ebx + 0x18))();
    return;
}

void sub_4d0() {
    return;
}

void sub_4d5() {
    *(int8_t *)eax = *(int8_t *)eax + eax;
    *(int8_t *)eax = *(int8_t *)eax + eax;
    return;
}

void sub_4ff() {
    return;
}

void sub_500() {
    *(int8_t *)eax = *(int8_t *)eax + eax;
    *(int8_t *)eax = *(int8_t *)eax + eax;
    *(int8_t *)eax = *(int8_t *)eax + eax;
    *(int8_t *)eax = *(int8_t *)eax + eax;
    *(int8_t *)eax = *(int8_t *)eax + eax;
    *(int8_t *)eax = *(int8_t *)eax + eax;
    *(int8_t *)eax = *(int8_t *)eax + eax;
    *(int8_t *)eax = *(int8_t *)eax + eax;
    return;
}

void sub_685() {
    return;
}
